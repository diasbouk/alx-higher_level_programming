#include "lists.h"

/**
 * insert_node - Function that inserts a new node in a linked_list
 * @head: head of the list
 * @number: data of new node
 * Return: Adress of new node or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *copy = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (number < (*head)->n)
	{
		new->next = copy;
		*head = new;
		return (new);
	}

	while (number > copy->n)
	{
		if (copy == NULL || copy->next == NULL)
			return (NULL);

		copy = copy->next;
	}

	new->next = copy->next;
	copy->next = new;
    new->n = copy->n;
    copy->n = number;

	return (new);
}