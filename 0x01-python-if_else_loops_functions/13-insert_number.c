#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: pointer to the start of the linked list
 * @number: node to be inserted
 * Return: listint_t with inserted node, NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || ((*head)->n > number))
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (*head);
}
