package dataprocessing.processors.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import dataprocessing.beans.Book;
import dataprocessing.beans.MainObject;
import dataprocessing.processor;
import dataprocessing.reusables.Location;

import java.io.File;
import java.io.IOException;

public class JsonProcessor implements processor {

    public void proccessdata(Object o) {
        ObjectMapper jsonMapper = new ObjectMapper();
        File jsonFileLocation = new File((String) o);

        try {
            MainObject book = jsonMapper.readValue(jsonFileLocation,MainObject.class);
            System.out.println(book.getBook().getAuthor());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Object process(Object o) {
        return null;
    }

    /**
     * return get data
     */
    public void getData() {

    }

    public static void main(String[] args) {
        JsonProcessor processor = new JsonProcessor();
        processor.proccessdata(Location.resource+"/json/book.json");

    }
}
