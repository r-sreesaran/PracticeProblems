package dataprocessing.processors.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import dataprocessing.beans.Book;
import dataprocessing.processor;
import com.fasterxml.jackson.dataformat.csv.CsvFactory;
import dataprocessing.reusables.Location;

import java.io.File;
import java.io.IOException;

public class CsvProcessor<T> implements processor {
    public void proccessdata(Object o) {
        File csvFileLocation = new File((String) o);
        ObjectMapper csvMapper = new ObjectMapper(new CsvFactory());

        try {
            Book book = csvMapper.readValue(csvFileLocation,Book.class);
            System.out.println(book.getAuthor());
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public Object process(Object o) {
        return null;
    }

    public static void main(String[] args) {
        CsvProcessor processor = new CsvProcessor();
        processor.proccessdata(Location.resource+"/csv/book.csv");

    }
}
