#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - create empty list and check if it is a palindrome
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);

	return (0);
}