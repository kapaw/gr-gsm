#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Decode Raw
# Generated: Thu Nov 19 04:32:49 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import pi
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import grgsm
import pmt
import sip
import sys

from distutils.version import StrictVersion
class decode_raw(gr.top_block, Qt.QWidget):

    def __init__(self, gain=30, ppm=0, samp_rate=2000000.052982, shiftoff=400e3, fc=943.6e6):
        gr.top_block.__init__(self, "Decode Raw")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Decode Raw")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "decode_raw")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.gain = gain
        self.ppm = ppm
        self.samp_rate = samp_rate
        self.shiftoff = shiftoff
        self.fc = fc

        ##################################################
        # Variables
        ##################################################
        self.ppm_slider = ppm_slider = ppm
        self.g_slider = g_slider = gain
        self.fc_slider = fc_slider = fc

        ##################################################
        # Blocks
        ##################################################
        self._fc_slider_layout = Qt.QVBoxLayout()
        self._fc_slider_tool_bar = Qt.QToolBar(self)
        self._fc_slider_layout.addWidget(self._fc_slider_tool_bar)
        self._fc_slider_tool_bar.addWidget(Qt.QLabel("Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._fc_slider_counter = qwt_counter_pyslot()
        self._fc_slider_counter.setRange(925e6, 1990e6, 2e5)
        self._fc_slider_counter.setNumButtons(2)
        self._fc_slider_counter.setValue(self.fc_slider)
        self._fc_slider_tool_bar.addWidget(self._fc_slider_counter)
        self._fc_slider_counter.valueChanged.connect(self.set_fc_slider)
        self._fc_slider_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._fc_slider_slider.setRange(925e6, 1990e6, 2e5)
        self._fc_slider_slider.setValue(self.fc_slider)
        self._fc_slider_slider.setMinimumWidth(100)
        self._fc_slider_slider.valueChanged.connect(self.set_fc_slider)
        self._fc_slider_layout.addWidget(self._fc_slider_slider)
        self.top_layout.addLayout(self._fc_slider_layout)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	fc_slider, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._ppm_slider_layout = Qt.QHBoxLayout()
        self._ppm_slider_layout.addWidget(Qt.QLabel("PPM Offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._ppm_slider_counter = qwt_counter_pyslot()
        self._ppm_slider_counter.setRange(-150, 150, 1)
        self._ppm_slider_counter.setNumButtons(2)
        self._ppm_slider_counter.setMinimumWidth(100)
        self._ppm_slider_counter.setValue(self.ppm_slider)
        self._ppm_slider_layout.addWidget(self._ppm_slider_counter)
        self._ppm_slider_counter.valueChanged.connect(self.set_ppm_slider)
        self.top_layout.addLayout(self._ppm_slider_layout)
        self.gsm_sdcch8_demapper_0 = grgsm.universal_ctrl_chans_demapper(1, ([0,4,8,12,16,20,24,28,32,36,40,44]), ([8,8,8,8,8,8,8,8,136,136,136,136]))
        self.gsm_receiver_0 = grgsm.receiver(4, ([0]), ([]))
        self.gsm_message_printer_1 = grgsm.message_printer(pmt.intern(""), False,
            False, False)
        self.gsm_input_0 = grgsm.gsm_input(
            ppm=0,
            osr=4,
            fc=fc,
            samp_rate_in=samp_rate,
        )
        self.gsm_decryption_0 = grgsm.decryption(([]), 1)
        self.gsm_control_channels_decoder_0_0 = grgsm.control_channels_decoder()
        self.gsm_control_channels_decoder_0 = grgsm.control_channels_decoder()
        self.gsm_clock_offset_control_0 = grgsm.clock_offset_control(fc-shiftoff)
        self.gsm_bcch_ccch_demapper_0 = grgsm.universal_ctrl_chans_demapper(0, ([2,6,12,16,22,26,32,36,42,46]), ([1,2,2,2,2,2,2,2,2,2]))
        self._g_slider_layout = Qt.QHBoxLayout()
        self._g_slider_layout.addWidget(Qt.QLabel("Gain"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._g_slider_counter = qwt_counter_pyslot()
        self._g_slider_counter.setRange(0, 50, 0.5)
        self._g_slider_counter.setNumButtons(2)
        self._g_slider_counter.setMinimumWidth(100)
        self._g_slider_counter.setValue(self.g_slider)
        self._g_slider_layout.addWidget(self._g_slider_counter)
        self._g_slider_counter.valueChanged.connect(self.set_g_slider)
        self.top_layout.addLayout(self._g_slider_layout)
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_SERVER", "127.0.0.1", "4729", 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "4729", 10000, False)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-2*pi*shiftoff/samp_rate)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/tmp/gsm_raw", False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_rotator_cc_0, 0), (self.gsm_input_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.gsm_input_0, 0), (self.gsm_receiver_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_rotator_cc_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.gsm_bcch_ccch_demapper_0, "bursts", self.gsm_control_channels_decoder_0, "bursts")
        self.msg_connect(self.gsm_clock_offset_control_0, "ppm", self.gsm_input_0, "ppm_in")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_control_channels_decoder_0_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_control_channels_decoder_0_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_decryption_0, "bursts", self.gsm_control_channels_decoder_0_0, "bursts")
        self.msg_connect(self.gsm_receiver_0, "C0", self.gsm_bcch_ccch_demapper_0, "bursts")
        self.msg_connect(self.gsm_receiver_0, "C0", self.gsm_sdcch8_demapper_0, "bursts")
        self.msg_connect(self.gsm_receiver_0, "measurements", self.gsm_clock_offset_control_0, "measurements")
        self.msg_connect(self.gsm_sdcch8_demapper_0, "bursts", self.gsm_decryption_0, "bursts")

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "decode_raw")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_g_slider(self.gain)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.set_ppm_slider(self.ppm)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.gsm_input_0.set_samp_rate_in(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fc_slider, self.samp_rate)
        self.blocks_rotator_cc_0.set_phase_inc(-2*pi*self.shiftoff/self.samp_rate)

    def get_shiftoff(self):
        return self.shiftoff

    def set_shiftoff(self, shiftoff):
        self.shiftoff = shiftoff
        self.blocks_rotator_cc_0.set_phase_inc(-2*pi*self.shiftoff/self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.gsm_input_0.set_fc(self.fc)
        self.set_fc_slider(self.fc)

    def get_ppm_slider(self):
        return self.ppm_slider

    def set_ppm_slider(self, ppm_slider):
        self.ppm_slider = ppm_slider
        Qt.QMetaObject.invokeMethod(self._ppm_slider_counter, "setValue", Qt.Q_ARG("double", self.ppm_slider))

    def get_g_slider(self):
        return self.g_slider

    def set_g_slider(self, g_slider):
        self.g_slider = g_slider
        Qt.QMetaObject.invokeMethod(self._g_slider_counter, "setValue", Qt.Q_ARG("double", self.g_slider))

    def get_fc_slider(self):
        return self.fc_slider

    def set_fc_slider(self, fc_slider):
        self.fc_slider = fc_slider
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fc_slider, self.samp_rate)
        Qt.QMetaObject.invokeMethod(self._fc_slider_counter, "setValue", Qt.Q_ARG("double", self.fc_slider))
        Qt.QMetaObject.invokeMethod(self._fc_slider_slider, "setValue", Qt.Q_ARG("double", self.fc_slider))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set gain [default=%default]")
    parser.add_option("-p", "--ppm", dest="ppm", type="intx", default=0,
        help="Set ppm [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(2000000.052982),
        help="Set samp_rate [default=%default]")
    parser.add_option("-o", "--shiftoff", dest="shiftoff", type="eng_float", default=eng_notation.num_to_str(400e3),
        help="Set shiftoff [default=%default]")
    parser.add_option("-f", "--fc", dest="fc", type="eng_float", default=eng_notation.num_to_str(943.6e6),
        help="Set fc [default=%default]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = decode_raw(gain=options.gain, ppm=options.ppm, samp_rate=options.samp_rate, shiftoff=options.shiftoff, fc=options.fc)
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
