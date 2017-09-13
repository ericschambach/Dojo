using System;
using System.Collections.Generic;

namespace cardeck
{
    public class Deck
    {
        
        List<string> myDeck = new List<string>();
        string myNewCard;

        public Deck(string[] myDeck,string myNewCard)
        {
            Random rand = new Random();
            for(int i = 1; i <= 52; i++)
            {
                int x = rand.Next(0,14);
                int y = rand.Next(0,4);
                string cardName = myCards.cardArr[i];

                {
                    while(arrNums.Contains(x))
                    {
                        x = rand.Next(5,25);                    
                    }
                }
            
        }

        // public string stringVal()
        // {   

        //     string[] cardArr = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
        //     Random rand = new Random();
        //     string x = cardArr[rand.Next(0,cardArr.Length)];
        //     return x;
        // }
        // public string suit()
        // {
        //     string[] cardSuit = {"Clubs", "Spades", "Hearts", "Diamonds"};
        //     Random rand = new Random();
        //     string x = cardSuit[rand.Next(0,cardSuit.Length)];
        //     return x;
        // }
        // public int val()
        // {
        //     int[] cardVal = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
        //     int x = 0;
        //     return x;

        // }
    }
}