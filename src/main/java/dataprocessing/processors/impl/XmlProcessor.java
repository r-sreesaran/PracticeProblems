package dataprocessing.processors.impl;



import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import dataprocessing.beans.Book;
import dataprocessing.processor;
import dataprocessing.reusables.Location;

import java.io.*;

public class XmlProcessor<T> implements processor
{
    public void proccessdata(Object o) {
        File xmlFileLocation = new File((String) o);
        ObjectMapper xmlMapper = new XmlMapper();

        try {
            Book book = xmlMapper.readValue(xmlFileLocation,Book.class);
            System.out.println(book.getAuthor());
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
        XmlProcessor processor = new XmlProcessor();
        processor.proccessdata(Location.resource+"/xml/data.xml");

    }
}
