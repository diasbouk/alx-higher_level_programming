#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	if (!(*head) || !(*head)->next)
		return (1);
	while (temp)
	{
		while ((*head)->next)
			*head = (*head)->next;
		if((*head)->n != temp->n)
			return (0);
		else
		{
			temp = temp->next;
			*head = temp;
		}
	}
	return (1);
}
