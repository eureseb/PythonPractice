#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
    1. Get lower case from s1 to a string
    2. Get lower case from s2 to a strings
    3. For each letter from both strings, get the maximum from both.
    4. Print the resulting string in descending order the amount
    each letter repeats(get this from the max(s1[letter],s2[letter]))
    language = "Number:char*number/ + "
*/
char whatPrefix(int n){
    if(n == 1)
        return '1';
    else if(n == 2)
        return '2';
    return '=';
}
int isLower(char c){
    if(c >= 'a' && c <= 'z') return 1;
    return 0;
}
char* get_lower_case(char str[]){
    char* res = (char*)malloc(sizeof(char*)*100);
    int i = 0, j = 0;
    while(str[i] != '\0'){        
        if(isLower(str[i]) == 1){
            res[j++] = str[i];
        }
        i++;
    }
    res[j] = '\0';
    return res;
}
int* count_letters(char* str){
    int* map = (int*)malloc(sizeof(int)*26);
    for(int i = 0; i < 26; i++){
        map[i] = 0;
    }
    int i = 0, j = 0;
    while(str[i] != '\0'){        
        map[str[i]-'a']++;
        i++;
    }
    
    return map;
}
char *mix(char* str1,char* str2 ){
    char* res = (char*)malloc(sizeof(char*)*100);
    
    char* lc_str1 = get_lower_case(str1);
    char* lc_str2 = get_lower_case(str2);

    int* map2 = count_letters(lc_str1);
    int* map1 = count_letters(lc_str2);
    int* res_map = (int*)malloc(sizeof(int)*26);
    int* what_string = (int*)malloc(sizeof(int)*26);

    int h_count = 0;
    int res_count = 0;
    for(int i = 0; i < 26; i++){
        res_map[i] = 0;
        if(map1[i] > h_count) h_count = map1[i];
        else if(map2[i] > h_count) h_count = map2[i];
        // printf("map2:%d map1:%d\n",map2[i],map1[i]);
        if(map1[i] > 1 || map2[i] > 1){
            if(map1[i] == map2[i]){
                res_map[i] = map1[i];
                what_string[i] = 3;
            }else if(map1[i] > map2[i]){
                res_map[i] = map1[i];
                what_string[i] = 1;
            }else if(map2[i] > map1[i]){
                res_map[i] = map2[i];
                what_string[i] = 2;
            }
        }
    }

    for(int i=h_count+1; i>=2; i--){
        for(int j=0;j<26;j++){
            if(map2[j] < map1[j] && i == res_map[j]){
                res[res_count++] = whatPrefix(what_string[j]);
                res[res_count++] = ':';
                for(int k=0; k<i; k++){
                    res[res_count++] = 'a' + j ;
                }
                res[res_count++] = '/';
            }
        }
        for(int j=0;j<26;j++){
            if(map2[j] > map1[j] && i == res_map[j]){
                res[res_count++] = whatPrefix(what_string[j]);
                res[res_count++] = ':';
                for(int k=0; k<i; k++){
                    res[res_count++] = 'a' + j ;
                }
                res[res_count++] = '/';
            }
        }
        for(int j=0;j<26;j++){
            if(map2[j] == map1[j] && i == res_map[j]){
                res[res_count++] = whatPrefix(what_string[j]);
                res[res_count++] = ':';
                for(int k=0; k<i; k++){
                    res[res_count++] = 'a' + j ;
                }
                res[res_count++] = '/';
            }
        }
            
    }
    res[res_count-1] = '\0';
    return res;
}
int main(){
    char str1[] = "looping is fun but dangerous";
    char str2[] = "less dangerous than coding";
    char c = 'a';
    printf("%s",mix(str1,str2));

    return 0;
}