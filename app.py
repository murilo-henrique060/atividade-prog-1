from flet import app, Page
import router

def main(page: Page):
  router.init(page)
  page.on_route_change = router.navigate
  page.go("login")

if __name__ == "__main__":
  app(target=main)