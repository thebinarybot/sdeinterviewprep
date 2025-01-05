public class rabinkarp {
    public static void main(String[] args) {
        String text = "interviewprepPREP";
        String pattern = "PREP";
        System.out.println("Substring Found At Index: " + RabinKarp(text, pattern));
    }

    public static int RabinKarp(String text, String pattern) {
        int primeModulous = 101;
        int patternLength = pattern.length();
        int textLength = text.length();
        int alphabetSize = 256;
        int hashFactor = (int) Math.pow(alphabetSize, patternLength - 1) % primeModulous;
        int patternHash = 0;
        int currentWindowHash = 0;

        // Preprocessing
        for (int i = 0; i < patternLength; i++) {
            patternHash = (alphabetSize * patternHash + pattern.charAt(i)) % primeModulous;
            currentWindowHash = (alphabetSize * currentWindowHash + text.charAt(i)) % primeModulous;
        }

        // Slide over the text
        for (int i = 0; i <= textLength - patternLength; i++) { 
            if (patternHash == currentWindowHash) {
                boolean isMatch = true;
                // Verification to minimize collision
                for (int j = 0; j < patternLength; j++) { 
                    if (text.charAt(i + j) != pattern.charAt(j)) {
                        isMatch = false;
                        break;
                    }
                }
                if (isMatch) {
                    return i;
                }
            }

            // Slide window by removing the leftmost and adding the immediate right
            if (i < textLength - patternLength) {
                currentWindowHash = (alphabetSize * (currentWindowHash - text.charAt(i) * hashFactor) + text.charAt(i + patternLength)) % primeModulous;
                if (currentWindowHash < 0) {
                    currentWindowHash += primeModulous;
                }
            }
        }

        // If there is no match, return -1
        return -1;
    }
}
