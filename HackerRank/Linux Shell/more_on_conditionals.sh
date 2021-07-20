#!/bin/bash
read sideOne 
read sideTwo 
read sideThree

if [[ $sideOne == $sideTwo ]] && [[ $sideTwo == $sideThree ]] 
then 
    echo "EQUILATERAL"
elif [[ $sideOne == $sideTwo ]] || [[ $sideTwo == $sideThree ]]|| [[ $sideOne == $sideThree ]] 
then 
    echo "ISOSCELES"
else 
    echo "SCALENE"
fi