package dataprocessing;

public interface processor<T> {
    public void proccessdata(T t);

    public T process(T t);

}
