import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

css = b"""
#puke {
       background: red;
}

"""

style_provider = Gtk.CssProvider()
style_provider.load_from_data(css)

class HelloWorldWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="LinuxAtPUKE")
		self.button = Gtk.Button(label="CLICKEAMEE")
		self.button.set_name("puke")
		self.button.connect("clicked", self.on_button_clicked)

		self.add(self.button)

	def on_button_clicked(self, widget):
		print ("wsp dude? | LinuxAtPUKE | :D")



def main():

	win = HelloWorldWindow()

	Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
	)

	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()



if __name__ == '__main__':
	main()
