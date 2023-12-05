#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palidrome - check the code for
 * @head: head of a linked_list
 * Return: Always 0.
 */
 int is_palindrome(listint_t **head)
 {
   listint_t *temp = *head;
   int *list_count = NULL, i = 1, j = 0;

   if (!(*head) || !(*head)->next)
      return (1);
   while (temp)
   {
      temp = temp->next;
      i++;
   }
   list_count = (int *)malloc(i * sizeof(int));
   while (*head)
   {
      list_count[i] = (*head)->n;
      *head = (*head)->next;
   }

   while (j < i)
   {
      if (list_count[j] != list_count[i - 1])
         return (0);
      i--, j++;
   }
   return (1);
}