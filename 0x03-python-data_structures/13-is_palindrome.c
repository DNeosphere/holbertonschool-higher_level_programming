#include "lists.h"
/**
 * is_palindrome - finds palindromism in a list
 * @head: pointer to the first node
 * Return: retunr 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	size_t count = 0, len = 0, iter = 0;
	int buffer[1024];

	if (head == NULL)
		return (0);

	while (temp)
	{
		buffer[count] = temp->n;
		count++;
		temp = temp->next;
	}
	len = count -1;

	if (len <= 1)
		return (1);

	while (iter <= (len))
	{
		if (buffer[iter] != buffer[len])
			return (0);
		iter++;
		len--;
	}
	return (1);


}

