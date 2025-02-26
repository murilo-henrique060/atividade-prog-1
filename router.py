from flet import RouteChangeEvent, Page

from routes.login import login

def init(p: Page):
  """Inialize the router.
  """

  global page, routes, protected_routes
  page = p
  routes = { view.route: view for view in map(lambda view: view(page), [login]) }
  protected_routes = []

def navigate(e: RouteChangeEvent) -> None:
  """Route change event handler.

  Args:
      e (RouteChangeEvent): Route change event.
  """

  if e.route in routes:
    page.views.clear()
    page.views.append(routes[e.route])
    page.update()
  else:
    print(f"Route {e.route} not found")