Vagrant.configure("2") do |config|

  config.vm.define "scriptbox" do |scriptbox|
    scriptbox.vm.box = "ubuntu/trusty64"
	  scriptbox.vm.network "private_network", ip: "192.168.10.2"
    scriptbox.vm.hostname = "scriptbox"
   
  end
end
