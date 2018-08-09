<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="16008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="DomeCommunicator" Type="Folder">
			<Item Name="domeCommunicator.lvclass" Type="LVClass" URL="../domeCommunicator/domeCommunicator.lvclass"/>
			<Item Name="tcpDevice.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/tcpDevice/tcpDevice.lvclass"/>
		</Item>
		<Item Name="DomeController" Type="Folder">
			<Item Name="DomeController.lvclass" Type="LVClass" URL="../domeController/DomeController.lvclass"/>
			<Item Name="IDome.lvclass" Type="LVClass" URL="../IDome/IDome.lvclass"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="High Resolution Relative Seconds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Relative Seconds.vi"/>
			</Item>
			<Item Name="ComEvents.ctl" Type="VI" URL="../../common_labview_tcpdevice/ts_labview_tcp/tcpTypedefs/ComEvents.ctl"/>
			<Item Name="deviceHeartbeat.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/deviceHeartbeat/deviceHeartbeat.lvclass"/>
			<Item Name="deviceStatus.ctl" Type="VI" URL="../../common_labview_tcpdevice/typedefs/deviceStatus.ctl"/>
			<Item Name="heartbeat.ctl" Type="VI" URL="../../common_labview_tcpdevice/typedefs/heartbeat.ctl"/>
			<Item Name="messageEnd.ctl" Type="VI" URL="../../common_labview_tcpdevice/typedefs/messageEnd.ctl"/>
			<Item Name="statusEnum.ctl" Type="VI" URL="../../common_labview_tcpdevice/typedefs/statusEnum.ctl"/>
			<Item Name="TCPClient.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/ts_labview_tcp/TCPClient/TCPClient.lvclass"/>
			<Item Name="TCPComEvents.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/ts_labview_tcp/TCPComEvents/TCPComEvents.lvclass"/>
			<Item Name="TCPCommunicator.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/ts_labview_tcp/TCPCommunicator/TCPCommunicator.lvclass"/>
			<Item Name="TCPSettings.ctl" Type="VI" URL="../../common_labview_tcpdevice/ts_labview_tcp/tcpTypedefs/TCPSettings.ctl"/>
			<Item Name="TCPSettings.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/ts_labview_tcp/TCPSettings/TCPSettings.lvclass"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
