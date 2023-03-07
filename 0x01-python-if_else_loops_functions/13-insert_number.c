#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - Insert a node in an ordered singly linked list
 * @head: head of the list
 * @number: number to be inserted
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous, *new;

	current = *head;
	previous = NULL;
	while (current->next != NULL)
	{
		if (number < current->n)
			break;
		previous = current;
		current = current->next;
	}

	new = malloc(sizeof(listint_t));
	new->next = current;
	new->n = number;
	previous->next = new;
	return (new);
}
