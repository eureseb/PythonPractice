#include <stdio.h>

int duplicate_count(const char *text) {
  int alpha[36] = {0};
  int res = 0;
    while(text[i] != '\0'){
        
        // printf("%d,", alpha[i]);
        if(text[i] >= 'a' && text[i] <= 'z')
            alpha[text[i]-'a']+=1;
        else if(text[i] >= 'A' && text[i] <= 'Z') 
            alpha[text[i]-'A']++;
        else if(text[i] >= '0' && text[i] <= '9') 
            alpha[text[i]-'0'+26]++;
            
        i++;
        
    }
    for(i=0; i<36; i++){
        if(alpha[i] > 1){
            res++;
        }
    }
     return res;
}
// int duplicate_count(const char *text) {
//   int i = 0;
//   int alpha[36] = {0};
//   int res = 0;
//     while(text[i] != '\0'){
//         // printf("%d,", alpha[i]);
//         if(text[i] >= 'a' && text[i] <= 'z')
//             alpha[text[i]-'a']+=1;
//         else if(text[i] >= 'A' && text[i] <= 'Z') 
//             alpha[text[i]-'A']++;
//         else if(text[i] >= '0' && text[i] <= '9') 
//             alpha[text[i]-'0'+26]++;
            
//         i++;
        
//     }
//     for(i=0; i<36; i++){
//         if(alpha[i] > 1){
//             res++;
//         }
//     }
//      return res;
// }