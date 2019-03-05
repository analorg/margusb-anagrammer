import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.nio.charset.Charset;


public class Anagrammer{

    public static void main(String[] args) {
        
        long start = System.nanoTime();
        String res = "";

        String filePath = "data/google-10000-english.txt"; 
        String word = "test"; 
        if(args.length >= 2){
            filePath = (!args[0].isEmpty() && args[0] != null ) ? args[0].replace("\'", "") : filePath; 
            word = (!args[1].isEmpty() && args[1] != null ) ? args[1].replace("\'", "") : word; 
        }
        
        try {
            res = anagrammer(filePath, word);
        } catch (Exception e) {
            res ="";
        }
        
        long end = System.nanoTime();
        long microseconds = (end - start) / 1000;

        //System.out.println();
        if(!res.isEmpty())
        {
            System.out.println(microseconds + res);
        }
   
    }

    public static String anagrammer(String filePath, String word) throws FileNotFoundException, IOException
    {
                String res = "";
                //System.out.println("Filepath: " + filePath);
                //System.out.println("Word: " + word);
        
                HashMap<String, String> dict = new HashMap<String, String>();
                dict = read_dictionary_file(filePath);
                //dict.forEach((k,v) -> System.out.println(k + "/" + v));
                
                HashSet<String> anagrams = new HashSet<String>();
                anagrams = findAnagrams(dict, word);
                           
                res = conventAnagramsToList(anagrams);
        
        return res;
    }


    public static HashMap<String, String> read_dictionary_file(String filePath) throws IOException
    {

        HashMap<String, String> dict = new HashMap<String, String>();
        File file = new File(filePath);
        String line = "";
        //BufferedReader buffReader = new BufferedReader(new FileReader(file));
        Charset inputCharset = Charset.forName("ISO-8859-1"); 
        BufferedReader buffReader = new BufferedReader(new InputStreamReader(new FileInputStream(file), inputCharset));
     
         while((line = buffReader.readLine())!= null){
            
            String key = line.strip().replace(" ", "|");
            String value = encodeAnagrams(line.strip()); 
            dict.put(key, value);
            
        }
        buffReader.close();
        
        return dict;
    }

    public static String encodeAnagrams(String word)
    {
        String value = sortString(word);
        return  value;
    }

    public static HashSet<String> findAnagrams(HashMap<String, String> dict, String word)
    {
        HashSet<String> anagrams = new HashSet<String>();
        
        // https://stackoverflow.com/questions/46898/how-do-i-efficiently-iterate-over-each-entry-in-a-java-map
        word = sortString(word);
        for(String key : dict.keySet()){
            if(dict.get(key).equalsIgnoreCase(word)){
                anagrams.add(key.replace("|", " "));
            }
          
        }
        return anagrams;
        
    }

    public static String conventAnagramsToList(HashSet<String> anagrams)
    {
        StringBuilder res = new StringBuilder();
        for (String s : anagrams) {
            res.append(",").append(s);
        }
        return res.toString();

    }

    public static String sortString(String inputString) 
    { 
        char tempArray[] = inputString.toCharArray(); 
        Arrays.sort(tempArray); 
        return new String(tempArray); 
    } 


}