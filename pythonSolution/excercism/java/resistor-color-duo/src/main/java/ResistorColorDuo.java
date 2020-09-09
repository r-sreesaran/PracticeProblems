import java.util.Map;
import java.util.LinkedHashMap;


class ResistorColorDuo {
     Map<String,String> map = new LinkedHashMap<>();
    String resistanceValue = "";
       ResistorColorDuo() {
              map.put("black","0");
              map.put("brown","1");
              map.put("red","2");
              map.put("orange","3");
              map.put("yellow","4");
              map.put("green","5");
              map.put("blue","6");
              map.put("violet","7");
              map.put("grey","8");
              map.put("white","9");
              }

    int value(String[] colors) {
        
        resistanceValue = "";
        for(int i = 0;i<2;i++) {
            resistanceValue = resistanceValue + map.get(colors[i]);
        }
        return Integer.parseInt(resistanceValue);
    }
}
