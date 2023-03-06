#include <stdio.h>
#include <string.h>

int main () {
   char command[50];

   //strcpy( command, "dir" );
   //strcpy( command, "ls -al" );
   system(command);

   return(0);
} 