#include "lists.h"

/**
 * check_cycle - function that checks if a linked
 * list has a cycle or not .
 * @list: linked list to check .
 * Return: 1 if a cylce is found , 0 if not .
*/

int check_cycle(listint_t *list)
{
    if (list == NULL)
        return (0);

    while (list)
    {
        list = list->next;
        if (list->n > -1)
            return (1);
    }
    return(0);
}