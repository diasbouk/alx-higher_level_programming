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
   i = 0;
   while (*head)
   {
      list_count[i] = (*head)->n;
      *head = (*head)->next;
   }

   while (j < i - 1)
   {
      if (list_count[j] != list_count[i])
         return (0);
      i++, j++;
   }
   return (1);
}