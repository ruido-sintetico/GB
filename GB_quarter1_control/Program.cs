// See https://aka.ms/new-console-template for more information
Console.WriteLine("Quarter 1 Choice Specialization Controle Work");
string[] strings = CreateArray();
string[] newString = NoMoreThreeLettersString(strings);
PrintArray(newString);

string[] NoMoreThreeLettersString(string[] arr) {
    string[] newArr = new string[NumberElementsLessThreeSymbols(arr)];
    int count = 0;
    for(int i = 0; i < arr.Length; i++){
        if(arr[i].Length > 2) {
            newArr[count] = arr[i];
            ++count;
        }
    }
    return newArr;

}

int NumberElementsLessThreeSymbols(string[] arr) {

    int num = 0;

    for(int i = 0; i < arr.Length; i++) {

        if(arr[i].Length > 2) ++num;

    }

    return num;

}

void PrintArray(string[] array) {
    Console.Write("[");

    for (int i = 0; i < array.Length; i++)
    {
        if(i == array.Length - 1) Console.Write($"{array[i]}");
        else Console.Write($"{array[i]}, ");
    }

    Console.Write("]");
    Console.WriteLine();
};

string[] CreateArray() {

    Console.WriteLine("Write some text.");
    string s = Console.ReadLine();

    string[] subs = s.Split(" ");

    return subs;

}