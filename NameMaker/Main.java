import java.util.Random;

public class Main {
    private static final String VOWELS = "aeiou";
    private static final String CONSONANTS = "bcdfghjklmnpqrstvwxyz";
    private static final Random random = new Random();
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please add a name to the commandline");
            return;
        }

        // We are not using any uppercase in our constant variables
        String name = args[0].toLowerCase();

        // Get them as an array of vowels and consonants
        String asVAndC = transpose(name);

        // Randomly pick characters from them to make the final name
        String finalName = getFinalName(asVAndC);
        System.out.println(finalName);
    }

    private static String transpose(String initialName) {
        String finStr = "";
        for (String character : initialName.split("")) {
            if (VOWELS.contains(character)) {
                finStr = finStr.concat("v");
            } else if (CONSONANTS.contains(character)) {
                finStr = finStr.concat("c");
            } else {
                finStr = finStr.concat(" ");
            }
        }
        return finStr;
    }

    private final static String getFinalName(String initialName) {
        String finStr = "";
        for (String character : initialName.split("")) {
            switch (character) {
                case "c" -> finStr = finStr.concat(pickRandom(CONSONANTS));
                case "v" -> finStr = finStr.concat(pickRandom(VOWELS));
                case " " -> finStr = finStr.concat(" ");
            }
        }
        return finStr;
    }

    private final static String pickRandom(String thisString) {
        char chosen = thisString.charAt(random.nextInt(thisString.length()));
        return Character.toString(chosen);
    }
}

