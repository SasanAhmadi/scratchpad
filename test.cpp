#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>

using namespace std;

ifstream infile("input.txt");

map<string, float> calculatePlayerStat(map<char, int> codes){
  // initialize result map with zero values 
  map<string, float> result;
  result.insert({"BA", 0});
  result.insert({"OB%", 0});
  result.insert({"K", 0});
  result.insert({"BB", 0});
  result.insert({"HBP", 0});
  result.insert({"H", 0});

  int total = 0;
  for (const auto &p : codes){
    total+=p.second;
  }

  int outs = codes.count('O') ? codes['O'] : 0;
  
  result["H"] = codes.count('H') ? codes['H'] : 0;
  result["HBP"] = codes.count('P') ? codes['P'] : 0;
  result["BB"] = codes.count('W') ? codes['W'] : 0;
  result["K"] = codes.count('K') ? codes['K'] : 0;
  result["OB%"] = (result["H"] + result["BB"] + result["HBP"])/total;

  float atbats = result["H"] + outs + result["K"];
  result["BA"] = result["H"] / atbats;

  return result;
}

string calculateLeaders(string item, map<string, map<string, float>> collection){
  map<string, float> playerItemValues;
  for (const auto &p : collection){
    playerItemValues.insert({p.first, ((map<string, float>)p.second)[item]});
  }
  auto pr = max_element(playerItemValues.begin(), playerItemValues.end(), [](const auto &x, const auto &y) {
          return x.second < y.second;
      });
  float max_value = pr->second;
  string result;
  for (const auto &p : collection) {
    if (((map<string, float>)p.second)[item] == max_value){
      result += p.first + " ";
    }
  }
  result += to_string(max_value);
  return result;
}

int main() {

  // lets create a map to store each each player and its codes,
  // codes will be another map to store each code and number f times it is occurring for that player 
  map< string, map<string, float> > playersStats;
  
  for( string line; getline( infile, line ); )
  {
    // this is the delimeter to split the line value to two part, name and codes
    string delimiter = " ";

    // extract name from line string by substring function
    // name starts from index 0 to where delimiter occurs
    string name = line.substr(0, line.find(delimiter));

    // extract codes, this will start from delimiter to the end of the string, so the remaining len for substr would be whole line length - name length 
    string codes = line.substr(line.find(delimiter)+1, line.length() - name.length());

    // lets create a map to store each code and number of times it is occurring in the code section: map(char, int)
    map<char, int> scores;

    // do a loop over codes characters
    for(string::size_type i = 0; i < codes.size(); ++i) {
      // if the code NOT exists in map, add it with initial value 1
      if (scores.find(codes[i]) == scores.end()) {
        scores.insert({codes[i], 1});
      } else {
        // if exists, increases the value by 1
        scores[codes[i]]++;
      }
    }

    map<string, float> stats = calculatePlayerStat(scores);
    // this will insert each player(key) along with scores(value) to result map{key, value} 
    playersStats.insert({name, stats});
  }

  // this is to output the resulting map 
  for (const auto &p : playersStats) {
    cout << p.first << "\n";

    map<string, float> item = ((map<string, float>)p.second);
    cout << "BA: " << item["BA"] << "\n";
    cout << "OB%: " << item["OB%"] << "\n";
    cout << "H: " << item["H"] << "\n";
    cout << "BB: " << item["BB"] << "\n";
    cout << "K: " << item["K"] << "\n";
    cout << "HBP: " << item["HBP"] << "\n";
    cout << "\n";
  }

  cout << "LEAGUE LEADERS\n";
  cout << "BA: " << calculateLeaders("BA", playersStats) << "\n";
  cout << "OB%: " << calculateLeaders("OB%", playersStats) << "\n";
  cout << "H: " << calculateLeaders("H", playersStats) << "\n";
  cout << "BB: " << calculateLeaders("BB", playersStats) << "\n";
  cout << "K: " << calculateLeaders("K", playersStats) << "\n";
  cout << "HBP: " << calculateLeaders("HBP", playersStats) << "\n";
  
}
