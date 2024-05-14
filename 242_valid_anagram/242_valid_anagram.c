bool isAnagram(char* s, char* t) {
        if (strlen(s) != strlen(t)) {
        return false;
    }
    
    // Array to count frequency of each character (assuming only lowercase letters)
    int count[26] = {0};
    
    // Count characters in s
    for (int i = 0; s[i] != '\0'; i++) {
        count[s[i] - 'a']++;
    }
    
    // Subtract counts based on characters in t
    for (int i = 0; t[i] != '\0'; i++) {
        count[t[i] - 'a']--;
    }
    
    // Check if all counts are zero
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            return false;
        }
    }
    
    return true;
}
