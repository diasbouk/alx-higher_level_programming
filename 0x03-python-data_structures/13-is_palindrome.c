#include "lists.h"

/**
 * is_palindrome - check the code for
 * @head: head of a linked_list
 * Return: Always 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

		if (!(*head) || !(*head)->next)
			return (1);
		while (temp)
		{
			while ((*head)->next)
				*head = (*head)->next;
			if ((*head)->next->n != temp->n)
				return (0);

			temp = temp->next;
			free((*head)->next);
			*head = temp;
		}
		return (1);
}
