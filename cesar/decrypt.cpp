#include <string>
#include <iostream>
#include <fstream>
#include <map>

int main(int argc, char const *argv[])
{
    std::string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,";
    std::map<char, int> alpha;
    for(int i = 0; i < alphabet.size(); i++){
        alpha[alphabet[i]] = i;
    }

    std::ifstream text(argv[1]);
    std::string line, encodedmsg = ""; 
    while(getline(text, line)){
        encodedmsg += line + "\n";
    }
    
    std::string decodedmsg = "";
    int aux;
    for(int i = 1; i < alphabet.size(); i++){
        for(int k = 0; k < encodedmsg.size(); k ++){
            if(alpha.find(encodedmsg[k]) != alpha.end()){
                aux = alpha.find(encodedmsg[k])->second;
                if(aux - i < 0){
                    aux = alphabet.size() + (aux - i);
                } else {
                    aux = aux - i;
                }
                decodedmsg += alphabet[aux];
            } else {
                decodedmsg += encodedmsg[k];
            }    
        }
        std::ofstream file("results/text" + std::to_string(i));
        file << decodedmsg;
        decodedmsg = "";
        file.close(); 
    }   
    return 0;
}
