using System.Runtime.CompilerServices;

Console.WriteLine("2");

var fileName = "C:/Users/Passi/Code/AdventOfCode2024/1/1/input"; //Should be copied to solution if you dont want to hardcode

var lines = File.ReadAllLines(fileName);
List<int> list1 = [];
Dictionary<int, int> occurences2 = [];
for (var i = 0; i < lines.Length; i += 1)
{
    var lineElements = lines[i].Split("   ");
    var input1 = int.Parse(lineElements[0]);
    var input2 = int.Parse(lineElements[1]);

    list1.Add(input1);
    occurences2[input2] = occurences2.GetValueOrDefault(input2)+1;
}


var similarityScoresSum = list1.Select((number, index) => number * occurences2.GetValueOrDefault(number)).Aggregate(0, (agg, x) => agg + x);

Console.WriteLine(similarityScoresSum);