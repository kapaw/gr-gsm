#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Decode Bursts Nogui
# Generated: Thu Nov 19 04:18:39 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import pi
from optparse import OptionParser
import grgsm
import pmt

class decode_bursts_nogui(gr.top_block):

    def __init__(self, fc=943.6e6, shiftoff=400e3, ppm=0, gain=30, samp_rate=2000000.052982):
        gr.top_block.__init__(self, "Decode Bursts Nogui")

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
        self.gsm_sdcch8_demapper_0 = grgsm.universal_ctrl_chans_demapper(1, ([0,4,8,12,16,20,24,28,32,36,40,44]), ([8,8,8,8,8,8,8,8,136,136,136,136]))
        self.gsm_message_printer_1 = grgsm.message_printer(pmt.intern(""), False,
            False, False)
        self.gsm_decryption_0 = grgsm.decryption(([]), 1)
        self.gsm_control_channels_decoder_0_0 = grgsm.control_channels_decoder()
        self.gsm_control_channels_decoder_0 = grgsm.control_channels_decoder()
        self.gsm_burst_file_source_0 = grgsm.burst_file_source("/tmp/bursts")
        self.gsm_bcch_ccch_demapper_0 = grgsm.universal_ctrl_chans_demapper(0, ([2,6,12,16,22,26,32,36,42,46]), ([1,2,2,2,2,2,2,2,2,2]))
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_SERVER", "127.0.0.1", "4729", 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "4729", 10000, False)

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.gsm_sdcch8_demapper_0, "bursts", self.gsm_decryption_0, "bursts")
        self.msg_connect(self.gsm_decryption_0, "bursts", self.gsm_control_channels_decoder_0_0, "bursts")
        self.msg_connect(self.gsm_control_channels_decoder_0_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_control_channels_decoder_0_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_bcch_ccch_demapper_0, "bursts", self.gsm_control_channels_decoder_0, "bursts")
        self.msg_connect(self.gsm_burst_file_source_0, "out", self.gsm_bcch_ccch_demapper_0, "bursts")
        self.msg_connect(self.gsm_burst_file_source_0, "out", self.gsm_sdcch8_demapper_0, "bursts")


    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_shiftoff(self):
        return self.shiftoff

    def set_shiftoff(self, shiftoff):
        self.shiftoff = shiftoff

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

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
    tb = decode_bursts_nogui(fc=options.fc, shiftoff=options.shiftoff, ppm=options.ppm, gain=options.gain, samp_rate=options.samp_rate)
    tb.start()
    tb.wait()
