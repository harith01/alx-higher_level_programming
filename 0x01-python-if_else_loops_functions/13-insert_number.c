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
	listint_t *current, *new;

	new = malloc(sizeof(listint_t));
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		new->n = number;
	}
	else
	{
		current = *head;
		while (current->next != NULL)
		{
			if (current->next->n < number)
			{
				current = current->next;
				break;
			}
		}
		new->next = current->next;
		new->n = number;
		current->next = new;
	}
	return (new);
}
