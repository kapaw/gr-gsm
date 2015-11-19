#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Capture Raw Nogui
# Generated: Thu Nov 19 04:29:24 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import pi
from optparse import OptionParser
import osmosdr

class capture_raw_nogui(gr.top_block):

    def __init__(self, fc=943.6e6, shiftoff=400e3, ppm=0, gain=30, samp_rate=2000000.052982):
        gr.top_block.__init__(self, "Capture Raw Nogui")

        ##################################################
        # Parameters
        ##################################################
        self.fc = fc
        self.shiftoff = shiftoff
        self.ppm = ppm
        self.gain = gain
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(fc-shiftoff, 0)
        self.rtlsdr_source_0.set_freq_corr(ppm, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(250e3+abs(shiftoff), 0)
          
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/tmp/gsm_raw", False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_file_sink_0, 0))



    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.rtlsdr_source_0.set_center_freq(self.fc-self.shiftoff, 0)

    def get_shiftoff(self):
        return self.shiftoff

    def set_shiftoff(self, shiftoff):
        self.shiftoff = shiftoff
        self.rtlsdr_source_0.set_center_freq(self.fc-self.shiftoff, 0)
        self.rtlsdr_source_0.set_bandwidth(250e3+abs(self.shiftoff), 0)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.rtlsdr_source_0.set_freq_corr(self.ppm, 0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.rtlsdr_source_0.set_gain(self.gain, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-f", "--fc", dest="fc", type="eng_float", default=eng_notation.num_to_str(943.6e6),
        help="Set fc [default=%default]")
    parser.add_option("-o", "--shiftoff", dest="shiftoff", type="eng_float", default=eng_notation.num_to_str(400e3),
        help="Set shiftoff [default=%default]")
    parser.add_option("-p", "--ppm", dest="ppm", type="intx", default=0,
        help="Set ppm [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set gain [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(2000000.052982),
        help="Set samp_rate [default=%default]")
    (options, args) = parser.parse_args()
    tb = capture_raw_nogui(fc=options.fc, shiftoff=options.shiftoff, ppm=options.ppm, gain=options.gain, samp_rate=options.samp_rate)
    tb.start()
    tb.wait()
