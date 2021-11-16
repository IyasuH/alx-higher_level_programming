#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 *check_cycle - check wether the linked list is looped or not
 *@list: pointer to head of  list
 *Return: 1 or 0 (there is cycle or not)
 */
int check_cycle(listint_t *list)
{
unsigned int i = 0;
unsigned int n = 0;
n = print_listint(list);
 for(; i<n; i++)
   {
     list = list->next;
     if(list == NULL)
       return (0);
     else
       continue;
}
 return (1); 
}
