package dataprocessing.processors.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import dataprocessing.beans.Book;
import dataprocessing.processor;
import dataprocessing.reusables.Location;

import java.io.File;
import java.io.IOException;

public class YamlProcessor<T> implements processor {
    public void proccessdata(Object o) {
        ObjectMapper jsonMapper = new ObjectMapper(new YAMLFactory());
        File yamlFileLocation  = new File((String) o);

        try {
            Book book = jsonMapper.readValue(yamlFileLocation,Book.class);
            System.out.println(book.getAuthor());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Object process(Object o) {
        return null;
    }

    public static void main(String[] args) {
        YamlProcessor processor1 = new YamlProcessor();
        processor1.proccessdata(Location.resource+"/yaml/book.yaml");

    }
}
