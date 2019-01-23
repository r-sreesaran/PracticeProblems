package dataprocessing.processors.impl;



import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import dataprocessing.beans.Book;
import dataprocessing.processor;

import java.io.*;

public class XmlProcessor<T> implements processor
{

    public void proccessdata(Object o) {
        File xmlFileLocation = new File((String) o);
        ObjectMapper xmlMapper = new XmlMapper();

        try {
            Book book = xmlMapper.readValue(xmlFileLocation,Book.class);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public Object process(Object o) {
        return null;
    }

    public static void main(String[] args) {
        XmlProcessor processor = new XmlProcessor();
        processor.proccessdata("/Users/sree/Documents/opensource/github/CodeChefPracticeProblems/src/main/java/dataprocessing/processors/resources/xml/book.xml");

    }
}
