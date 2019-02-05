package dataprocessing.processors.impl;

import com.fasterxml.jackson.databind.MappingIterator;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.csv.CsvMapper;
import com.fasterxml.jackson.dataformat.csv.CsvParser;
import dataprocessing.beans.Book;
import dataprocessing.processor;
import com.fasterxml.jackson.dataformat.csv.CsvFactory;
import dataprocessing.reusables.Location;

import java.io.File;
import java.io.IOException;

public class CsvProcessor<T> implements processor {
    public void proccessdata(Object o) {
        CsvMapper mapper = new CsvMapper();
        mapper.enable(CsvParser.Feature.WRAP_AS_ARRAY);
        File csvFile = new File((String) o);
        ObjectMapper csvMapper = new ObjectMapper(new CsvFactory());

        try {
            MappingIterator<String[]> it = mapper.readerFor(String[].class).readValues(csvFile);
            while (it.hasNext()) {
                String[] row = it.next();
                // and voila, column values in an array. Works with Lists as well
                System.out.println(row[1]);
            }

            //Book book = csvMapper.readValue(csvFileLocation,Book.class);
            //System.out.println(book.getAuthor());
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public Object process(Object o) {
        return null;
    }

    public void getData() {

    }

    public static void main(String[] args) {
        CsvProcessor processor = new CsvProcessor();
        processor.proccessdata(Location.resource+"/csv/book.csv");

    }
}
