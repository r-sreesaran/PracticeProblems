import java.util.Map;
import java.util.LinkedHashMap;

class ResistorColor {
    static Map<String,Integer> map = new LinkedHashMap<>();
       static {
              map.put("black",0);
              map.put("brown",1);
              map.put("red",2);
              map.put("orange",3);
              map.put("yellow",4);
              map.put("green",5);
              map.put("blue",6);
              map.put("violet",7);
              map.put("grey",8);
              map.put("white",9);
       }

    int colorCode(String color) {
        return map.get(color);
    }

    String[] colors() {
        return map.keySet().toArray(new String[map.size()]); 
    }
}
