package dataprocessing;

public interface processor<T> {
    public void proccessdata(T t);

    public T process(T t);

    /**
     * This mainly used converting bean back to data specified data format
     */
    public void getData();
}
