#!/usr/bin/python
#0603_other_strategies_multiple_choices.py by Sujit Dhamale
#to Understanding other strategies for multiple choices

def main():
    choices =dict(
        one='first',
        two='second',
        three='third',
        four='fourth',
        five='fifth'
        )

    v='six'
    #print(choices[v])
    print(choices.get(v, 'other'))



    
if __name__ == "__main__": main()
