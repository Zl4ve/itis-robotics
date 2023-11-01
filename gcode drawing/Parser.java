package ru.itis;

import java.io.*;

public class Parser {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream("source.txt")));
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("result.txt")))) {
            String c;
            while ((c = reader.readLine()) != null) {
                String[] arg = c.split(" ");
                if (arg[0].equals("G1")) {
                    Double x = null;
                    Double y = null;
                    for (String elem : arg) {
                        if (elem.startsWith("X")) {
                            x = Double.parseDouble(elem.substring(1));
                        } else if (elem.startsWith("Y")) {
                            y = Double.parseDouble(elem.substring(1));
                        }
                    }
                    if (!(x == null && y == null)) {
                        writer.write("movePenTo(" + x + ", " + y + ");\n");
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
