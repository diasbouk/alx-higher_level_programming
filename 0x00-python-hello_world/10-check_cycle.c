#include "lists.h"

/**
 * check_cycle - function that checks if a linked
 * list has a cycle or not .
 * @list: linked list to check .
 * Return: 1 if a cylce is found , 0 if not .
*/

int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    if (list == NULL || list->next == NULL)
        return (0);
        
        
    while (fast)
    {
        if (fast->next == slow)
            return (1);
        if (fast->next == NULL)
            return (0);
       fast = fast->next->next;
       slow = slow->next;
    }
    return(0);
}