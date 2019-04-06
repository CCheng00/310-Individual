import opennlp.tools.namefind.NameFinderME;
import opennlp.tools.namefind.TokenNameFinderModel;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.util.Span;

import py4j.GatewayServer;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

public class EntityRecognition {

    public static void main(String[] args) {
        System.out.println("Opening gateway...");
        EntityRecognition app = new EntityRecognition();
        GatewayServer server = new GatewayServer(app);
        server.start();
    }

    public static String trimmer(String input){
        String tokens[] = {};
        Span spans[] = {};
        int begs[] = new int[input.length()];
        int ends[] = new int[input.length()];
        int count = 0;
        String trimmed = "";
        try {
            InputStream tokenStream = new FileInputStream("en-token.bin");

            InputStream locationModelStream = new FileInputStream(new File("en-ner-location.bin"));

            TokenizerModel tm = new TokenizerModel(tokenStream);

            TokenizerME tokenizer = new TokenizerME(tm);

            TokenNameFinderModel tnfm = new TokenNameFinderModel(locationModelStream);

            NameFinderME nf = new NameFinderME(tnfm);

            tokens = tokenizer.tokenize(input);

            spans = nf.find(tokens);
        }
        catch(Exception e){
        }

        for(int i = 0; i < spans.length; i++){
            begs[count] = Character.getNumericValue(spans[i].toString().charAt(1));
            ends[count] = Character.getNumericValue(spans[i].toString().charAt(4));
            count++;
        }

        for(int i = 0; i < count; i++){
            for(int j = begs[i]; j < ends[i]; j++){
                tokens[j] = null;
            }
        }

        for(int i = 0; i < tokens.length; i++){
            if(tokens[i]!=null){
                trimmed+=tokens[i] + " ";
            }
        }

        return trimmed;
    }


    }
