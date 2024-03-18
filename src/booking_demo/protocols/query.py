from typing import List
 
from uagents import Context, Model, Protocol


""""
 
TableStatus: this represents the status of a table and includes the attributes 
number of seats, start time, and end time.
QueryTableRequest: this is used for querying table availability. 
It includes information about the number of guests, start time, and duration
of the table request.
QueryTableResponse: this contains the response to the query table availability.
It includes a list of table numbers that are available based on query parameters.
GetTotalQueries: this is used to request the total number of queries made to the system.
TotalQueries: this contains the response to the total queries request, 
including the count of total queries made to the system.

"""
class TableStatus(Model):
    seats: int
    time_start: int
    time_end: int
class QueryTableRequest(Model):
    guests: int
    time_start: int
    duration: int
class QueryTableResponse(Model):
    tables: List[int]
class GetTotalQueries(Model):
    pass
class TotalQueries(Model):
    total_queries: int
query_proto = Protocol()
 
@query_proto.on_message(model=QueryTableRequest, replies=QueryTableResponse)
async def handle_query_request(ctx: Context, sender: str, msg: QueryTableRequest):
    tables = {
        int(num): TableStatus(**status)
        for (
            num,
            status,
        ) in ctx.storage._data.items()
        if isinstance(num, int)
    }
    available_tables = []
    for number, status in tables.items():
        if (
            status.seats >= msg.guests
            and status.time_start <= msg.time_start
            and status.time_end >= msg.time_start + msg.duration
        ):
            available_tables.append(int(number))
    ctx.logger.info(f"Query: {msg}. Available tables: {available_tables}.")
    await ctx.send(sender, QueryTableResponse(tables=available_tables))
    total_queries = int(ctx.storage.get("total_queries") or 0)
    ctx.storage.set("total_queries", total_queries + 1)
 
@query_proto.on_query(model=GetTotalQueries, replies=TotalQueries)
async def handle_get_total_queries(ctx: Context, sender: str, _msg: GetTotalQueries):
    total_queries = int(ctx.storage.get("total_queries") or 0)
    await ctx.send(sender, TotalQueries(total_queries=total_queries))
    
    
    
    """
    handle_query_request(): this message handler function is defined using the .on_message() decorator. 
    It handles the QueryTableRequest messages and replies with a QueryTableResponse message. 
    The handler processes the table availability query based on the provided parameters, 
    checks the table statuses stored in the agent's storage, 
    and sends the available table numbers as a response to the querying agent. Additionally, the handler tracks the total number of queries made and increments the count in storage.

    handle_get_total_queries(): this message handler function is defined using the
    .on_query() decorator. It handles the GetTotalQueries query and replies with a 
    TotalQueries message containing the total number of queries made to the system. The handler retrieves the total query count from the agent's storage and responds with the count.
    """