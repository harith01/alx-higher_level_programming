#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: pointer to the first element
 * Return: 1 if it has a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t slow_p = list, fast_p = list;
	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
