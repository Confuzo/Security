#include <string>
#include <iostream>
#include <fstream>
#include <map>

int main(int argc, char const *argv[])
{
    std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::map<char, int> alpha;
    for(int i = 0; i < alphabet.size(); i++){
        alpha[alphabet[i]] = i;
    }

    std::ifstream text(argv[1]);
    std::string line, encodedmsg = ""; 
    while(getline(text, line)){
        encodedmsg += line + "\n";
    }
    std::string key(argv[2]);
    
    std::string decodedmsg = "";
    int aux_key = 0;
    int aux;
    for(int i = 0; i < encodedmsg.size(); i++){
        if(alpha.find(encodedmsg[i]) != alpha.end()){
            aux = alpha.find(encodedmsg[i])->second - alpha.find(key[aux_key])->second;
            if(aux < 0){
                aux += 26;
            }
            aux_key++;
            decodedmsg += alphabet[aux];
            if(aux_key == key.size()){
                aux_key = 0;
            }
        } else {
            decodedmsg += encodedmsg[i];
        }
    }
    std::cout << decodedmsg;
    return 0;
}
