#include <stdio.h>
#include <stdlib.h>

char square[10] = {'0','1','2','3','4','5','6','7','8','9'};
int win();
int board();
int main(){
    int player,i,choice,random,flag;
    char mark;
    printf("YOU ARE PLAYER 1 AND BY DEFAULT YOU ARE 'X'");
    do{
        board();
        printf("enter '1' if its your chance: ");
    scanf("%d",&player);
        if(player == 1){
            printf("player1 enter choice: ");
            scanf("%d",&choice);
            flag = choice;
            mark = 'x';

        }
        else {

                flag!=choice;
                random = rand()%10;
                choice = random;
                mark = 'o';

                //if(1 != choice){

                //}
        }
        if(choice == 1&&square[1]=='1')
            square[1]=mark;
        else if(choice == 2&&square[2]=='2')
            square[2]=mark;
        else if(choice == 3&&square[3]=='3')
            square[3]=mark;
        else if(choice == 4&&square[4]=='4')
            square[4]=mark;
        else if(choice == 5&&square[5]=='5')
            square[5]=mark;
        else if(choice == 6&&square[6]=='6')
            square[6]=mark;
        else if(choice == 7&&square[7]=='7')
            square[7]=mark;
        else if(choice == 8&&square[8]=='8')
            square[8]=mark;
        else if(choice == 9&&square[9]=='9')
            square[9]=mark;
        else{
            printf("invalid choice");
            player--;
        }
        i = win();
        player++;
    }while(i==-1);
    board();
    if(i==1){
        printf("player %d won",--player);
    }
    else{
        printf("tie");
    }
    return 0;
}
int win(){
    if(square[1]==square[2]&&square[2]==square[3]){
        return 1;
    }
    else if(square[4]==square[5]&&square[5]==square[6]){
        return 1;
    }
    else if(square[7]==square[8]&&square[8]==square[9]){
        return 1;
    }
    else if(square[1]==square[5]&&square[5]==square[9]){
        return 1;
    }
    else if(square[3]==square[5]&&square[5]==square[7]){
        return 1;
    }
    else if(square[1]==square[4]&&square[4]==square[7]){
        return 1;
    }
    else if(square[2]==square[5]&&square[5]==square[8]){
        return 1;
    }
    else if(square[3]==square[6]&&square[6]==square[9]){
        return 1;
    }
    else if(square[1]!='1' &&square[2]!='2' &&square[3]!='3' &&square[4]!='4' &&square[5]!='5' &&square[6]!='6' &&square[7]!='7' &&square[8]!='8' &&square[9]!='9'){
        return 0;
    }
    else{
        return -1;
    }
}
int board(){
    printf("  TIC TAC TOE  \n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[1],square[2],square[3]);
    printf("___|___|___\n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[4],square[5],square[6]);
    printf("___|___|___\n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[7],square[8],square[9]);
    printf("   |   |   \n");

}

/*
char square[10] = {'0','1','2','3','4','5','6','7','8','9'};
int win();
int board();
int main(){
    int player=1,i,choice,choice1,choice2=0,random,flag=1,j=0;
    int chance = 0;
    char mark;
    char chose[] = {};
    printf("YOU ARE PLAYER 1 AND BY DEFAULT YOU ARE 'X'\n");
    do{
        board();
        if(player%2 != 0){
            printf("player1 enter choice: ");
            scanf("%d",&choice1);
            //flag = choice;
            mark = 'x';
            j = 1;

        }
        else if(player%2==0){

                //flag!=choice;
                random = rand()%10;
                choice2 = random;
                mark = 'o';

                //if(1 != choice){

                //}
        }
        //else{
         //   continue;
        //}
        if(choice1 == choice2){
        if(player%2 !=0){
            choice = choice1;
        }
        if(player%2 ==0){
            choice = choice2;
        }
        if(choice == 1&&square[1]=='1')
            square[1]=mark;
        if(choice == 2&&square[2]=='2')
            square[2]=mark;
        if(choice == 3&&square[3]=='3')
            square[3]=mark;
        if(choice == 4&&square[4]=='4')
            square[4]=mark;
        if(choice == 5&&square[5]=='5')
            square[5]=mark;
        if(choice == 6&&square[6]=='6')
            square[6]=mark;
        if(choice == 7&&square[7]=='7')
            square[7]=mark;
        if(choice == 8&&square[8]=='8')
            square[8]=mark;
        if(choice == 9&&square[9]=='9')
            square[9]=mark;
        else{
            printf("invalid choice\n");
            player--;
        }
        }
        else{
            player--;
        }
        i = win();
        player++;
    }while(i==-1);
    board();
    if(i==1 && player%2 == 0){
        printf("player1 won");
    }
    else if(i==1 && player%2 !=0){
        printf("computer won");
    }
    else{
        printf("tie");
    }
    return 0;
}
int win(){
    if(square[1]==square[2]&&square[2]==square[3]){
        return 1;
    }
    else if(square[4]==square[5]&&square[5]==square[6]){
        return 1;
    }
    else if(square[7]==square[8]&&square[8]==square[9]){
        return 1;
    }
    else if(square[1]==square[5]&&square[5]==square[9]){
        return 1;
    }
    else if(square[3]==square[5]&&square[5]==square[7]){
        return 1;
    }
    else if(square[1]==square[4]&&square[4]==square[7]){
        return 1;
    }
    else if(square[2]==square[5]&&square[5]==square[8]){
        return 1;
    }
    else if(square[3]==square[6]&&square[6]==square[9]){
        return 1;
    }
    else if(square[1]!='1' &&square[2]!='2' &&square[3]!='3' &&square[4]!='4' &&square[5]!='5' &&square[6]!='6' &&square[7]!='7' &&square[8]!='8' &&square[9]!='9'){
        return 0;
    }
    else{
        return -1;
    }
}
int board(){
    printf("  TIC TAC TOE  \n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[1],square[2],square[3]);
    printf("___|___|___\n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[4],square[5],square[6]);
    printf("___|___|___\n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[7],square[8],square[9]);
    printf("   |   |   \n");

}
*/
/*
char square[10] = {'0','1','2','3','4','5','6','7','8','9'};
char chose[] = {}
int chance = 0;
int win();
int board();
int main(){
    int player=1,i,choice,random,flag=1,j=0;
    char mark;
    printf("YOU ARE PLAYER 1 AND BY DEFAULT YOU ARE 'X'\n");
    do{
        board();
        if(player%2 != 0){
            printf("player1 enter choice: ");
            scanf("%d",&choice);
            //flag = choice;
            mark = 'x';
            j = 1;

        }
        else if(player%2==0){

                //flag!=choice;
                random = rand()%10;
                choice = random;
                mark = 'o';

                //if(1 != choice){

                //}
        }

        //else{
         //   continue;
        //}
        if(choice == 1&&square[1]=='1')
            square[1]=mark;
        if(choice == 2&&square[2]=='2')
            square[2]=mark;
        if(choice == 3&&square[3]=='3')
            square[3]=mark;
        if(choice == 4&&square[4]=='4')
            square[4]=mark;
        if(choice == 5&&square[5]=='5')
            square[5]=mark;
        if(choice == 6&&square[6]=='6')
            square[6]=mark;
        if(choice == 7&&square[7]=='7')
            square[7]=mark;
        if(choice == 8&&square[8]=='8')
            square[8]=mark;
        if(choice == 9&&square[9]=='9')
            square[9]=mark;
        //else{
            //printf("invalid choice");
            //player--;
        //}
        if(choice>10){
            printf("invalid");
        }
        i = win();
        player++;
    }while(i==-1);
    board();
    if(i==1 && player%2 == 0){
        printf("player1 won");
    }
    else if(i==1 && player%2 !=0){
        printf("computer won");
    }
    else{
        printf("tie");
    }
    return 0;
}
int win(){
    if(square[1]==square[2]&&square[2]==square[3]){
        return 1;
    }
    else if(square[4]==square[5]&&square[5]==square[6]){
        return 1;
    }
    else if(square[7]==square[8]&&square[8]==square[9]){
        return 1;
    }
    else if(square[1]==square[5]&&square[5]==square[9]){
        return 1;
    }
    else if(square[3]==square[5]&&square[5]==square[7]){
        return 1;
    }
    else if(square[1]==square[4]&&square[4]==square[7]){
        return 1;
    }
    else if(square[2]==square[5]&&square[5]==square[8]){
        return 1;
    }
    else if(square[3]==square[6]&&square[6]==square[9]){
        return 1;
    }
    else if(square[1]!='1' &&square[2]!='2' &&square[3]!='3' &&square[4]!='4' &&square[5]!='5' &&square[6]!='6' &&square[7]!='7' &&square[8]!='8' &&square[9]!='9'){
        return 0;
    }
    else{
        return -1;
    }
}
int board(){
    printf("  TIC TAC TOE  \n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[1],square[2],square[3]);
    printf("___|___|___\n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[4],square[5],square[6]);
    printf("___|___|___\n");
    printf("   |   |   \n");
    printf("  %c|  %c|  %c\n",square[7],square[8],square[9]);
    printf("   |   |   \n");

}
*/
