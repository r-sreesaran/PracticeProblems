package dataprocessing.processors.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import dataprocessing.beans.Book;
import dataprocessing.processor;

import java.io.File;
import java.io.IOException;

public class JsonProcessor implements processor {
    public void proccessdata(Object o) {
        ObjectMapper jsonMapper = new ObjectMapper();
        File jsonFileLocation = new File((String) o);

        try {
            Book book = jsonMapper.readValue(jsonFileLocation,Book.class);
            System.out.println(book.getAuthor());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Object process(Object o) {
        return null;
    }

    public static void main(String[] args) {
        JsonProcessor processor = new JsonProcessor();
        processor.proccessdata();
    }
}
