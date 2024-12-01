Console.WriteLine("1");

var fileName = "C:/Users/Passi/Code/AdventOfCode2024/1/1/input"; //Should be copied to solution if you dont want to hardcode

var lines = File.ReadAllLines(fileName);
List<int> list1 = [];
List<int> list2 = [];
for (var i = 0; i < lines.Length; i += 1)
{
    var lineElements = lines[i].Split("   ");
    var input1 = int.Parse(lineElements[0]);
    var input2 = int.Parse(lineElements[1]);

    list1.Add(input1);
    list2.Add(input2);
}

list1.Sort();
list2.Sort();

var distances = list1.Zip(list2, (first, second) => Math.Abs(second - first));
var distancesSum = distances.Aggregate(0, (agg, x) => agg + x);

Console.WriteLine(distancesSum);