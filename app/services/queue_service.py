import json
import time
import redis

class RequestQueue:
    """
    A class representing a request queue for managing web crawling tasks, using Redis as the backend.

    This queue prioritizes tasks based on their content type, with different priorities assigned to HTML, images, videos, and other types.

    Methods:
    add_request(user_id, url, content_type): Adds a new request to the queue with a calculated priority.
    get_request(): Retrieves and removes the lowest-scored (highest priority) task from the queue.
    is_empty(): Checks if the queue is empty.
    print_queue(): Prints all tasks in the queue along with their priorities and scores.

    Attributes:
    redis (StrictRedis): A Redis client connected to the specified Redis server.
    queue_name (str): The name of the Redis sorted set used to store the queue.
    priority_map (dict): A mapping from content types to their corresponding priority scores.
    """
    def __init__(self) -> None:
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=1)
        self.queue_name = "request_queue"
        # Define a mapping from content types to priority scores
        self.priority_map = {
            'html': 10,
            'image': 5,
            'video': 1,
            'other': 3
        }

    def add_request(self, user_id, url, content_type):
        """
        Adds a new request to the queue with a priority based on the content type.

        Args:
        user_id: The user ID associated with the request.
        url: The URL to be crawled.
        content_type: The type of content expected at the URL.

        Returns:
        None
        """
        # Determine the priority based on content type
        priority = self.priority_map.get(content_type, self.priority_map['other'])
        task = json.dumps({'user_id': user_id, 'url': url, 'content_type': content_type})
        # Use current timestamp to differentiate tasks with the same priority
        timestamp = time.time()
        # Combine priority and timestamp to form a composite score
        score = -priority * 100000 + timestamp
        self.redis.zadd(self.queue_name, {task: score})

    def get_request(self):
        """
        Retrieves and removes the lowest-scored (highest priority) task from the queue.

        Returns:
        The task in JSON format if the queue is not empty, otherwise None.
        """
        packed_request = self.redis.zpopmin(self.queue_name)
        if packed_request:
            task_data, _ = packed_request[0]
            task = task_data.decode("utf-8")
            return task
        else:
            return None

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return self.redis.zcard(self.queue_name) == 0

    def print_queue(self):
        """
        Prints all tasks in the queue along with their priorities and scores.

        Returns:
        None
        """
        all_items_with_scores = self.redis.zrange(self.queue_name, 0, -1, withscores=True)
        for item, score in all_items_with_scores:
            task = json.loads(item.decode("utf-8"))
            print(f'User ID: {task["user_id"]}, URL: {task["url"]}, Content-Type: {task["content_type"]}, Priority: {score}')
