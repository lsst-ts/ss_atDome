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
			<Item Name="SmartdomeTypedefs" Type="Folder">
				<Item Name="commands.ctl" Type="VI" URL="../domeCommunicator/ComTypedefs/commands.ctl"/>
				<Item Name="domeState.ctl" Type="VI" URL="../IDome/domeTypedefs/domeState.ctl"/>
				<Item Name="openingStates.ctl" Type="VI" URL="../domeCommunicator/ComTypedefs/openingStates.ctl"/>
				<Item Name="queries.ctl" Type="VI" URL="../domeCommunicator/ComTypedefs/queries.ctl"/>
				<Item Name="shortStatus.ctl" Type="VI" URL="../domeCommunicator/ComTypedefs/shortStatus.ctl"/>
			</Item>
			<Item Name="DomeCommunicator.lvclass" Type="LVClass" URL="../domeCommunicator/DomeCommunicator.lvclass"/>
			<Item Name="tcpDevice.lvclass" Type="LVClass" URL="../../common_labview_tcpdevice/tcpDevice/tcpDevice.lvclass"/>
		</Item>
		<Item Name="DomeController" Type="Folder">
			<Item Name="DomeITypedefs" Type="Folder">
				<Item Name="azimuth.ctl" Type="VI" URL="../IDome/domeTypedefs/azimuth.ctl"/>
				<Item Name="direction.ctl" Type="VI" URL="../IDome/domeTypedefs/direction.ctl"/>
				<Item Name="motionDirection.ctl" Type="VI" URL="../IDome/domeTypedefs/motionDirection.ctl"/>
				<Item Name="openingMotion.ctl" Type="VI" URL="../IDome/domeTypedefs/openingMotion.ctl"/>
				<Item Name="openingPercentage.ctl" Type="VI" URL="../IDome/domeTypedefs/openingPercentage.ctl"/>
			</Item>
			<Item Name="DomeController.lvclass" Type="LVClass" URL="../domeController/DomeController.lvclass"/>
			<Item Name="DomeSimulator.lvclass" Type="LVClass" URL="../domeSimulator/DomeSimulator.lvclass"/>
			<Item Name="IDome.lvclass" Type="LVClass" URL="../IDome/IDome.lvclass"/>
		</Item>
		<Item Name="Test" Type="Folder">
			<Item Name="test.vi" Type="VI" URL="../domeController/test.vi"/>
			<Item Name="testVis.vi" Type="VI" URL="../test/testVis.vi"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="High Resolution Relative Seconds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Relative Seconds.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
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
